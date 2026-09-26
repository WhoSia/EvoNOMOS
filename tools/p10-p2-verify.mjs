#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

function die(msg) {
  console.error(msg);
  process.exit(1);
}

function load(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function hashFile(p) {
  const h = crypto.createHash('sha256');
  h.update(fs.readFileSync(p));
  return h.digest('hex');
}

const [directDir, invertDir, outPath] = process.argv.slice(2);
if (!directDir || !invertDir || !outPath) {
  die('usage: p10-p2-verify.mjs <direct-dir> <invert-dir> <out-json>');
}

function inspect(dir, expectedArm) {
  const receiptPath = path.join(dir, 'arm-receipt.json');
  const manifestPath = path.join(dir, 'materialization-manifest.json');
  if (!fs.existsSync(receiptPath) || !fs.existsSync(manifestPath)) {
    die(expectedArm + ': missing receipt or manifest');
  }
  const receipt = load(receiptPath);
  const manifest = load(manifestPath);
  if (receipt.arm !== expectedArm || manifest.arm !== expectedArm) {
    die(expectedArm + ': arm identity mismatch');
  }
  if (receipt.status !== 'PASS') die(expectedArm + ': receipt is not PASS');
  if (receipt.build !== 'PASS') die(expectedArm + ': build is not PASS');
  if (receipt.shared_oracle !== 'PASS') die(expectedArm + ': oracle is not PASS');
  if (receipt.reconstruction_verified !== true) {
    die(expectedArm + ': durable reconstruction is not verified');
  }
  if (receipt.comparative_metrics_opened !== false ||
      manifest.comparative_metrics_opened !== false) {
    die(expectedArm + ': comparative metric firewall breached');
  }
  if (receipt.winner !== null) die(expectedArm + ': winner must remain null');
  const bundlePath = path.join(dir, receipt.arm_bundle_file);
  if (!fs.existsSync(bundlePath)) die(expectedArm + ': bundle missing');
  if (hashFile(bundlePath) !== receipt.arm_bundle_sha256) {
    die(expectedArm + ': bundle digest mismatch');
  }
  if (receipt.contract_digest !== manifest.contract_digest) {
    die(expectedArm + ': contract digest mismatch inside arm');
  }
  if (receipt.base !== manifest.base) die(expectedArm + ': base mismatch inside arm');
  return { receipt, manifest };
}

const direct = inspect(directDir, 'DIRECT_DEDICATED');
const invert = inspect(invertDir, 'INVERT_CHANNEL_ADAPTER');

if (direct.receipt.base !== invert.receipt.base) {
  die('pair base mismatch');
}
if (direct.receipt.contract_digest !== invert.receipt.contract_digest) {
  die('pair contract digest mismatch');
}

const commonDirect = direct.receipt.common_file_sha256;
const commonInvert = invert.receipt.common_file_sha256;
const keysD = Object.keys(commonDirect).sort();
const keysI = Object.keys(commonInvert).sort();
if (JSON.stringify(keysD) !== JSON.stringify(keysI)) {
  die('common-file key set mismatch');
}
for (const key of keysD) {
  if (commonDirect[key] !== commonInvert[key]) {
    die('common file diverged across arms: ' + key);
  }
}

if (direct.receipt.arm_tree === invert.receipt.arm_tree) {
  die('treatment trees unexpectedly identical');
}

const seal = {
  stage: 'EvoNOMOS Generation VIII ORIGIN-R1-P10-P2',
  base: direct.receipt.base,
  contract_digest: direct.receipt.contract_digest,
  arms: {
    DIRECT_DEDICATED: {
      commit: direct.receipt.arm_commit,
      tree: direct.receipt.arm_tree,
      bundle_sha256: direct.receipt.arm_bundle_sha256,
    },
    INVERT_CHANNEL_ADAPTER: {
      commit: invert.receipt.arm_commit,
      tree: invert.receipt.arm_tree,
      bundle_sha256: invert.receipt.arm_bundle_sha256,
    },
  },
  gates: {
    build_admissibility: 'PASS',
    shared_oracle_equivalence: 'PASS',
    common_product_surface_byte_identity: 'PASS',
    durable_exact_arm_reconstruction: 'PASS',
    semantic_pair_comparability: 'PASS',
  },
  comparative_metrics_opened: false,
  lifecycle_measurement_authorized: true,
  winner: null,
  status: 'PASS_PAIR_COMPARABLE_DURABLE_CUSTODY',
};

fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(seal, null, 2) + '\n');
console.log('P10_P2_PAIR_COMPARABLE=PASS');
console.log('P10_P2_DURABLE_ARM_CUSTODY=PASS');
console.log('P10_P2_COMPARATIVE_METRICS_OPENED=NO');
