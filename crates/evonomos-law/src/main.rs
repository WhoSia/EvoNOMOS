use anyhow::{Context, Result};
use evonomos_law::{inspect, ModeratorEnvelope};
use std::{env, fs, path::PathBuf};

fn main() -> Result<()> {
    let mut args = env::args().skip(1);
    let command = args.next().unwrap_or_default();
    if command != "inspect" {
        anyhow::bail!("usage: evonomos-law inspect <moderator-json>");
    }
    let path = PathBuf::from(args.next().context("missing moderator-json path")?);
    if args.next().is_some() {
        anyhow::bail!("unexpected extra arguments");
    }

    let bytes = fs::read(&path).with_context(|| format!("read {}", path.display()))?;
    let env: ModeratorEnvelope =
        serde_json::from_slice(&bytes).with_context(|| format!("parse {}", path.display()))?;
    let out = inspect(env)?;
    println!("{}", serde_json::to_string_pretty(&out)?);
    Ok(())
}
