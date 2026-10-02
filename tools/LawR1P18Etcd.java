import java.nio.file.*;
import java.util.*;

public class LawR1P18Etcd {
    public static void main(String[] args) throws Exception {
        String input = args.length > 0 ? args[0] : "active/g8-law-r1-p18/P18_ETCD_FACTORIAL.tsv";
        String output = args.length > 1 ? args[1] : "out-p18/java-etcd.json";
        List<String> lines = Files.readAllLines(Path.of(input));
        int[][] y = new int[2][2];
        int rows = 0;
        for (int i = 1; i < lines.size(); i++) {
            if (lines.get(i).isBlank()) continue;
            String[] p = lines.get(i).split("\\t");
            int l = Integer.parseInt(p[0]);
            int g = Integer.parseInt(p[1]);
            y[l][g] = Integer.parseInt(p[2]);
            rows++;
        }
        boolean complete = rows == 4;
        boolean xnor = y[0][0] == 1 && y[0][1] == 0 && y[1][0] == 0 && y[1][1] == 1;
        int did = y[1][1] - y[1][0] - y[0][1] + y[0][0];
        boolean mainEffectOnlyRejected = did != 0;
        Files.createDirectories(Path.of("out-p18"));
        String json = String.format(Locale.ROOT,
            "{\n  \"tool\":\"java\",\n  \"complete_2x2\":%s,\n  \"xnor_reversal\":%s,\n  \"difference_in_differences\":%d,\n  \"main_effect_only_rejected\":%s,\n  \"interpretation\":\"Lifecycle mode reverses admissibility of local/older versus one-minor-higher version geometry.\"\n}\n",
            complete, xnor, did, mainEffectOnlyRejected);
        Files.writeString(Path.of(output), json);
        System.out.println("P18_JAVA_ETCD=" + (complete && xnor && mainEffectOnlyRejected ? "PASS" : "FAIL"));
        System.out.println("DID=" + did);
        if (!(complete && xnor && mainEffectOnlyRejected)) System.exit(2);
    }
}
