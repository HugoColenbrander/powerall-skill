#!/usr/bin/env bash
set -euo pipefail
# Powerall Connect API helper
# Env: POWERALL_TENANT, POWERALL_TOKEN, POWERALL_BASE_URL (default https://connect.powerall.io)
# Usage: powerall-api.sh GET /v1/relations
#        powerall-api.sh GET "/v1/products?limit=10&include=Supplier"
#        powerall-api.sh POST /v1/service-messages '{"field":"value"}'

METHOD="${1:-GET}"
ENDPOINT="${2:-}"
BODY="${3:-}"
BASE_URL="${POWERALL_BASE_URL:-https://connect.powerall.io}"
TENANT="${POWERALL_TENANT:-}"
TOKEN="${POWERALL_TOKEN:-}"

if [ -z "$TENANT" ] || [ -z "$TOKEN" ]; then
  echo "Set POWERALL_TENANT and POWERALL_TOKEN first." >&2; exit 1
fi
if [ -z "$ENDPOINT" ]; then
  echo "Usage: $0 <method> <endpoint> [body]" >&2; exit 1
fi

ARGS=(-sS -X "$METHOD" -u "$TENANT:$TOKEN" -H "Accept: application/json" -H "Content-Type: application/json" "${BASE_URL}${ENDPOINT}")
if [ -n "$BODY" ]; then ARGS=(-d "$BODY" "${ARGS[@]}"); fi

curl "${ARGS[@]}" | python3 -m json.tool 2>/dev/null || curl "${ARGS[@]}"
