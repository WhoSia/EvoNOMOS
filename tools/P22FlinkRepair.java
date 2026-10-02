import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class P22FlinkRepair {
    static final class CompatPayload implements Serializable {
        private static final long serialVersionUID = 2L;
        String value;
        CompatPayload(String value) { this.value = value; }
    }

    static final class OtherPayload implements Serializable {
        private static final long serialVersionUID = 2L;
        String value;
        OtherPayload(String value) { this.value = value; }
    }

    static byte[] serialize(Object x) throws Exception {
        ByteArrayOutputStream b = new ByteArrayOutputStream();
        try (ObjectOutputStream o = new ObjectOutputStream(b)) { o.writeObject(x); }
        return b.toByteArray();
    }

    static byte[] patchUID(byte[] input, Class<?> clazz, long uid) {
        byte[] out = input.clone();
        byte[] name = clazz.getName().getBytes(StandardCharsets.UTF_8);
        outer:
        for (int i=0;i+name.length+8<=out.length;i++) {
            for (int j=0;j<name.length;j++) if (out[i+j]!=name[j]) continue outer;
            int p=i+name.length;
            for (int k=7;k>=0;k--) { out[p+k]=(byte)(uid & 0xff); uid >>>= 8; }
            return out;
        }
        throw new IllegalStateException("class name not found");
    }

    static Object normal(byte[] bytes) throws Exception {
        try (ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(bytes))) {
            return in.readObject();
        }
    }

    static final class TargetedRepairInput extends ObjectInputStream {
        TargetedRepairInput(InputStream in) throws IOException { super(in); }
        @Override protected ObjectStreamClass readClassDescriptor() throws IOException, ClassNotFoundException {
            ObjectStreamClass stream = super.readClassDescriptor();
            if (stream.getName().equals(CompatPayload.class.getName()) && stream.getSerialVersionUID()==1L) {
                return ObjectStreamClass.lookup(CompatPayload.class);
            }
            return stream;
        }
    }

    static Object tolerant(byte[] bytes) throws Exception {
        try (ObjectInputStream in = new TargetedRepairInput(new ByteArrayInputStream(bytes))) {
            return in.readObject();
        }
    }

    static boolean failsNormal(byte[] bytes) {
        try { normal(bytes); return false; }
        catch (InvalidClassException expected) { return true; }
        catch (Exception other) { throw new RuntimeException(other); }
    }

    static boolean failsTolerant(byte[] bytes) {
        try { tolerant(bytes); return false; }
        catch (InvalidClassException expected) { return true; }
        catch (Exception other) { throw new RuntimeException(other); }
    }

    public static void main(String[] args) throws Exception {
        byte[] current=serialize(new CompatPayload("preserved"));
        byte[] old=patchUID(current, CompatPayload.class, 1L);

        CompatPayload direct=(CompatPayload)normal(current);
        boolean rawFails=failsNormal(old);
        CompatPayload repaired=(CompatPayload)tolerant(old);

        byte[] otherCurrent=serialize(new OtherPayload("other"));
        byte[] otherOld=patchUID(otherCurrent, OtherPayload.class, 1L);
        boolean nonTargetStillFails=failsTolerant(otherOld);

        boolean directPass="preserved".equals(direct.value);
        boolean repairPass="preserved".equals(repaired.value);

        Map<String,Object> m=new LinkedHashMap<>();
        m.put("stage","EvoNOMOS Generation VIII LAW-R1-P22");
        m.put("status", directPass && rawFails && repairPass && nonTargetStillFails ? "PASS":"FAIL");
        m.put("DIRECT_CURRENT", directPass ? "+":"-");
        m.put("OLD_RAW_MISMATCH", rawFails ? "-":"+");
        m.put("OLD_WITH_EXPLICIT_REPAIR", repairPass ? "+":"-");
        m.put("NON_TARGET_UID_MISMATCH_WITH_TOLERANT_READER", nonTargetStillFails ? "-":"+");
        m.put("repaired_value", repaired.value);
        m.put("targeted_repair_only", nonTargetStillFails);

        new File("out-p22").mkdirs();
        try (PrintWriter w=new PrintWriter("out-p22/p22-java.json")) {
            w.println("{");
            int i=0;
            for (var e:m.entrySet()) {
                String v = e.getValue() instanceof Boolean ? e.getValue().toString()
                    : "\"" + e.getValue().toString().replace("\\","\\\\").replace("\"","\\\"") + "\"";
                w.print("  \""+e.getKey()+"\": "+v);
                w.println(++i<m.size()?",":"");
            }
            w.println("}");
        }

        System.out.println("P22_FLINK_REPAIR="+m.get("status"));
        System.out.println("DIRECT_CURRENT="+m.get("DIRECT_CURRENT"));
        System.out.println("OLD_RAW_MISMATCH="+m.get("OLD_RAW_MISMATCH"));
        System.out.println("OLD_WITH_EXPLICIT_REPAIR="+m.get("OLD_WITH_EXPLICIT_REPAIR"));
        System.out.println("NON_TARGET="+m.get("NON_TARGET_UID_MISMATCH_WITH_TOLERANT_READER"));
        if (!"PASS".equals(m.get("status"))) System.exit(2);
    }
}
