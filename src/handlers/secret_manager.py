# Import the Secret Manager client library.
import os
from google.cloud import secretmanager


def get_secret(secret_id: str, version_id: str = 1) -> str:
    """
    Get information about the given secret version. It does not include the
    payload data.
    """

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    project_id = os.getenv('PID')

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Get the secret version.
    response = client.access_secret_version(request={"name": name})

    return response.payload.data.decode('UTF-8')
