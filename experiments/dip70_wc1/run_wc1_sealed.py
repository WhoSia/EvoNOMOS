#!/usr/bin/env python3
"""Pre-outcome sealed WC1 realization harness.

The first draft run_wc1.py was never executed. This wrapper corrects two
pre-execution representation bugs only: regex-source over-escaping and literal
${...} fixture escaping. It changes no preregistered policy, demand, follow-up,
metric, route, or oracle.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
import run_wc1 as m

m.INITIAL_RULES = (
    ("postgresql", "PostgreSQL", "database", (
        ("image", r"(?:image:\s*[^#\n]*(?:postgres(?:ql)?)(?::|@|\s|$))"),
        ("command", r"(?:command:\s*[^#\n]*\bpostgres(?:ql)?\b)"),
        ("environment", r"\bPOSTGRES_(?:DB|USER|PASSWORD|HOST_AUTH_METHOD)\b"),
    )),
    ("mysql-mariadb", "MySQL/MariaDB", "database", (
        ("image", r"(?:image:\s*[^#\n]*(?:mysql|mariadb)(?::|@|\s|$))"),
        ("command", r"(?:command:\s*[^#\n]*\b(?:mysqld|mariadbd)\b)"),
        ("environment", r"\b(?:MYSQL|MARIADB)_(?:DATABASE|USER|PASSWORD|ROOT_PASSWORD)\b"),
    )),
    ("redis", "Redis", "data service", (
        ("image", r"(?:image:\s*[^#\n]*redis(?::|@|\s|$))"),
        ("command", r"(?:command:\s*[^#\n]*\bredis-server\b)"),
        ("environment", r"\bREDIS_(?:URL|HOST|PORT|PASSWORD)\b"),
    )),
    ("rabbitmq", "RabbitMQ", "queue", (
        ("image", r"(?:image:\s*[^#\n]*rabbitmq(?::|@|\s|$))"),
        ("command", r"(?:command:\s*[^#\n]*\brabbitmq-server\b)"),
        ("environment", r"\bRABBITMQ_(?:DEFAULT_USER|DEFAULT_PASS|DEFAULT_VHOST|NODENAME)\b"),
    )),
    ("kafka-compatible", "Kafka-compatible", "broker", (
        ("image", r"(?:image:\s*[^#\n]*(?:confluentinc/cp-kafka|bitnami/kafka|apache/kafka|redpandadata/redpanda)(?::|@|\s|$))"),
        ("command", r"(?:command:\s*[^#\n]*(?:kafka-server-start|redpanda\s+start))"),
        ("environment", r"\b(?:KAFKA_(?:NODE_ID|PROCESS_ROLES|CONTROLLER_QUORUM_VOTERS)|KAFKA_CFG_[A-Z0-9_]+|REDPANDA_[A-Z0-9_]+)\b"),
    )),
)

m.FOLLOWUP_RULES = m.INITIAL_RULES + (
    ("mongodb", "MongoDB", "database", (
        ("image", r"(?:image:\s*[^#\n]*(?:mongo|mongodb)(?::|@|\s|$))"),
        ("command", r"(?:command:\s*[^#\n]*\b(?:mongod|mongos)\b)"),
        ("environment", r"\bMONGO_INITDB_(?:DATABASE|ROOT_USERNAME|ROOT_PASSWORD)\b"),
    )),
    ("nats-compatible", "NATS-compatible", "broker", (
        ("image", r"(?:image:\s*[^#\n]*nats(?::|@|\s|$))"),
        ("command", r"(?:command:\s*[^#\n]*\bnats-server\b)"),
        ("environment", r"\bNATS_(?:SERVER_NAME|CLUSTER_NAME|PORT|HTTP_PORT)\b"),
    )),
)

_original_tests_js = m.tests_js

def sealed_tests_js(followup=False):
    text = _original_tests_js(followup)
    return text.replace("${DB_IMAGE}", "\\${DB_IMAGE}").replace("${DB_NAME}", "\\${DB_NAME}")

m.tests_js = sealed_tests_js

if __name__ == "__main__":
    m.main()
