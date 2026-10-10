// P39-MATH-H: exhaustive seven-source-edit ternary cyclic-order shattering.
// A source edit is a vertex; every one-shot edit physically commutes and all
// orders are admissible, with separately queryable triple order parity.
// Pure finite mathematics, NOT real Go and NOT a pure-math priority claim.
#include <algorithm>
#include <array>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
constexpr int N=7, NUM=35, ROWS=720;
array<array<int,3>,NUM> triples{};
array<array<unsigned char,NUM>,ROWS> parity{};
array<bitset<ROWS>,NUM> yes{};
array<unsigned long long,9> fvector{};
vector<array<int,7>> shattered7;
array<int,8> selected{};

void enumerate(int depth,int next,const array<uint16_t,ROWS>& labels) {
    fvector[depth]++;
    if(depth==7) {
        array<int,7> h{};
        for(int i=0;i<7;i++)h[i]=selected[i];
        shattered7.push_back(h);
    }
    if(depth==8)return;
    for(int e=next;e<NUM;e++) {
        const int m=1<<(depth+1);
        array<bool,256> occurred{};
        array<uint16_t,ROWS> after{};
        for(int r=0;r<ROWS;r++) {
            const auto v=(uint16_t)(labels[r]|((uint16_t)parity[r][e]<<depth));
            after[r]=v;
            occurred[v]=true;
        }
        bool shattered=true;
        for(int j=0;j<m;j++)if(!occurred[j]){shattered=false;break;}
        if(shattered) {
            selected[depth]=e;
            enumerate(depth+1,e+1,after);
        }
    }
}
int main() {
    int z=0;
    for(int a=0;a<N;a++)
      for(int b=a+1;b<N;b++)
        for(int c=b+1;c<N;c++) triples[z++]={a,b,c};
    if(z!=NUM)return 1;
    array<int,N> order{0,1,2,3,4,5,6};
    int rows=0;
    do {
        // Cyclically shifting all seven edits preserves every triple parity.
        if(order[0]!=0)continue;
        array<int,N> rank{};
        for(int i=0;i<N;i++)rank[order[i]]=i;
        for(int e=0;e<NUM;e++) {
            auto [a,b,c]=triples[e];
            int sign=(rank[a]>rank[b])^(rank[a]>rank[c])^(rank[b]>rank[c]);
            parity[rows][e]=sign;
            yes[e].set(rows,sign);
        }
        rows++;
    } while(next_permutation(order.begin(),order.end()));
    if(rows!=ROWS)return 2;
    array<uint16_t,ROWS> initial{};
    enumerate(0,0,initial);
    const array<unsigned long long,9> expected{
        1,35,595,6405,46410,204246,274890,39930,0
    };
    if(fvector!=expected)return 3;
    cout<<"P39_H_EXACT_SHATTERING_F_VECTOR";
    for(int k=0;k<=8;k++)cout<<' '<<fvector[k];
    cout<<" PASS\n";
    if(shattered7.size()!=39930)return 4;
    unsigned long long checks=0;
    bool printed=false;
    // SECOND verification algorithm: reconstitute each depth-7 profile
    // from the original 720 rows as independent bitsets; try ALL 28 unused
    // queries, not only those after the highest index. Any shattered 8-set
    // must be reached from a shattered 7-set by removing one query.
    for(const auto& h:shattered7) {
        array<bitset<ROWS>,128> buckets{};
        for(int r=0;r<ROWS;r++) {
            unsigned int bits=0;
            for(int j=0;j<7;j++)bits|=(unsigned int)parity[r][h[j]]<<j;
            buckets[bits].set(r);
        }
        for(const auto& b:buckets)if(b.none())return 5;
        bitset<NUM> membership{};
        for(int e:h)membership.set(e);
        for(int e=0;e<NUM;e++) {
            if(membership[e])continue;
            checks++;
            bool extension=true;
            for(const auto& b:buckets) {
                if((b&yes[e]).none() || (b&(~yes[e])).none()) {
                    extension=false;
                    break;
                }
            }
            if(extension)return 6;
        }
        if(!printed) {
            cout<<"P39_H_SHATTERED_7_TRIPLES";
            for(int e:h) {
                const auto q=triples[e];
                cout<<' '<<q[0]<<q[1]<<q[2];
            }
            cout<<"\n";
            printed=true;
        }
    }
    if(checks!=1118040ULL)return 7;
    cout<<"P39_H_INDEPENDENT_7_TO_8_EXTENSION_COURT candidates="
        <<checks<<" no_success=1 PASS\n";
    cout<<"P39_H_THEOREM_D3_7_EQUALS_7_EXHAUSTIVE_PASS\n";
    return 0;
}
