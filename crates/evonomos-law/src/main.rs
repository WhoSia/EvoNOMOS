use anyhow::{Context, Result};
use evonomos_law::{adjudicate, inspect, AuthorityFirewall, LifecycleExposure, ModeratorEnvelope};
use serde::de::DeserializeOwned;
use std::{env, fs, path::PathBuf};

fn read_json<T: DeserializeOwned>(path: &PathBuf) -> Result<T> {
    let bytes = fs::read(path).with_context(|| format!("read {}", path.display()))?;
    serde_json::from_slice(&bytes).with_context(|| format!("parse {}", path.display()))
}

fn main() -> Result<()> {
    let mut args = env::args().skip(1);
    match args.next().as_deref() {
        Some("inspect") => {
            let path = PathBuf::from(args.next().context("missing moderator-json path")?);
            if args.next().is_some() {
                anyhow::bail!("unexpected extra arguments");
            }
            let env: ModeratorEnvelope = read_json(&path)?;
            println!("{}", serde_json::to_string_pretty(&inspect(env)?)?);
        }
        Some("adjudicate") => {
            let moderator = PathBuf::from(args.next().context("missing moderator-json path")?);
            let lifecycle = PathBuf::from(args.next().context("missing lifecycle-json path")?);
            let firewall = PathBuf::from(args.next().context("missing firewall-json path")?);
            if args.next().is_some() {
                anyhow::bail!("unexpected extra arguments");
            }
            let env: ModeratorEnvelope = read_json(&moderator)?;
            let lifecycle: LifecycleExposure = read_json(&lifecycle)?;
            let firewall: AuthorityFirewall = read_json(&firewall)?;
            println!(
                "{}",
                serde_json::to_string_pretty(&adjudicate(env, lifecycle, firewall)?)?
            );
        }
        _ => anyhow::bail!(
            "usage: evonomos-law inspect <moderator-json> | adjudicate <moderator-json> <lifecycle-json> <firewall-json>"
        ),
    }
    Ok(())
}
