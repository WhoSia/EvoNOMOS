using System;
using System.IO;
using System.Text.Json;

public class LawR1P18Boundary
{
    public static int Main(string[] args)
    {
        var input = args.Length > 0 ? args[0] : "active/g8-law-r1-p18/P18_NONBOT_INTERACTION_CUSTODY.json";
        var output = args.Length > 1 ? args[1] : "out-p18/csharp-boundary.json";
        using var doc = JsonDocument.Parse(File.ReadAllText(input));
        var root = doc.RootElement;
        var escape = root.GetProperty("domain_escape_readout");
        bool escaped = escape.GetProperty("bot_workflow_basin_escaped").GetBoolean();
        int exact = escape.GetProperty("exact_nonbot_family_count").GetInt32();
        bool second = escape.GetProperty("second_semantic_transport_family").GetBoolean();
        string target = root.GetProperty("primary_target_readout").GetProperty("COMPATIBILITY_X_COEXISTENCE").GetString() ?? "";
        string higher = root.GetProperty("higher_order_X").GetString() ?? "";
        bool conflict = root.GetProperty("same_normalized_X_G_E_conflicting_action_observed").GetBoolean();
        int negativeCount = root.GetProperty("negative_or_support_only_candidates").GetArrayLength();
        bool anti = root.GetProperty("post_hoc_X_additions").GetArrayLength() == 0 &&
                    root.GetProperty("post_hoc_interaction_subsets_added").GetArrayLength() == 0;
        string status = escaped && exact >= 1 && !second &&
                        target.StartsWith("UNDERIDENTIFIED") &&
                        higher == "UNDERIDENTIFIED" && !conflict && anti
            ? "PASS_PARTIAL_DOMAIN_ESCAPE"
            : "FAIL";
        Directory.CreateDirectory("out-p18");
        var payload = new {
            tool = "csharp",
            status,
            bot_workflow_basin_escaped = escaped,
            exact_nonbot_families = exact,
            second_transport = second,
            compatibility_x_coexistence = target,
            higher_order_x = higher,
            negative_candidate_count = negativeCount,
            anti_rationalization = anti,
            law_r2 = conflict ? "REOPEN_CANDIDATE" : "NOT_AUTHORIZED"
        };
        File.WriteAllText(output, JsonSerializer.Serialize(payload, new JsonSerializerOptions { WriteIndented = true }) + "\n");
        Console.WriteLine("P18_CSHARP_BOUNDARY=" + status);
        return status == "PASS_PARTIAL_DOMAIN_ESCAPE" ? 0 : 3;
    }
}
