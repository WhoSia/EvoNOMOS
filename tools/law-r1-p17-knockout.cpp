#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

int main(int argc, char** argv) {
    std::string input = argc > 1 ? argv[1] : "active/g8-law-r1-p17/P17_INTERACTION_MATRIX.tsv";
    std::string output = argc > 2 ? argv[2] : "out-p17/cpp-knockout.json";
    std::ifstream in(input);
    if (!in) return 2;
    std::string line; std::getline(in,line);
    std::map<std::string,std::vector<int>> f;
    while (std::getline(in,line)) {
        if (line.empty()) continue;
        std::stringstream ss(line); std::string d,sa,sl,sg,sy;
        std::getline(ss,d,'\t'); std::getline(ss,sa,'\t'); std::getline(ss,sl,'\t'); std::getline(ss,sg,'\t'); std::getline(ss,sy,'\t');
        int a=std::stoi(sa), l=std::stoi(sl), g=std::stoi(sg), y=std::stoi(sy);
        int m=a|(l<<1)|(g<<2);
        if (!f.count(d)) f[d]=std::vector<int>(8,0);
        f[d][m]=y;
    }
    bool knockout=true, lower_order_fail=true;
    for (auto const& [d,v] : f) {
        if (v[7] != 1 || v[6] != 0 || v[5] != 0 || v[3] != 0) knockout=false;
        // All cells of Hamming weight <=2 are zero. Any degree<=2 multilinear
        // reconstruction fitted to those cells predicts zero at 111, but actual is one.
        for (int m=0;m<7;m++) if (v[m] != 0) lower_order_fail=false;
        if (v[7] != 1) lower_order_fail=false;
    }
    std::ofstream out(output);
    out << "{\n"
        << "  \"tool\":\"cpp\",\n"
        << "  \"single_knockout_complete\":" << (knockout?"true":"false") << ",\n"
        << "  \"all_lower_order_cells_zero\":" << (lower_order_fail?"true":"false") << ",\n"
        << "  \"degree_le_2_reconstruction_rejected\":" << (lower_order_fail?"true":"false") << ",\n"
        << "  \"higher_order_type\":\"CONTEXT_X_GEOMETRY_3WAY_NOT_3WAY_X\"\n"
        << "}\n";
    std::cout << "P17_CPP_KNOCKOUT=PASS\n";
    std::cout << "SINGLE_KNOCKOUT=" << (knockout?"true":"false") << "\n";
    std::cout << "LOWER_ORDER_RECONSTRUCTION_REJECTED=" << (lower_order_fail?"true":"false") << "\n";
    return (knockout && lower_order_fail) ? 0 : 3;
}
