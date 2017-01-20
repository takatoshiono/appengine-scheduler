#!/bin/sh
DEPLOYABLE="$1"
GCLOUD="$HOME/Downloads/google-cloud-sdk/bin/gcloud"
"$GCLOUD" app deploy "$DEPLOYABLE" --project airy-highlander-792
