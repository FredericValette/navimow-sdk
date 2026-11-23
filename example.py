"""Navimow SDK Example Script.

Demonstrates how to activate and use MowerAPI and MowerClient to:
1. Connect via REST API using an OAuth access token
2. Discover robotic mower devices
3. Fetch device status (battery level, state, error status)
4. Send mower commands (start mowing, pause, return to dock, resume)
"""

import asyncio
import os
import sys
from typing import Any

import aiohttp
from mower_sdk import (
    MowerClient,
    MowerAPI,
    MowerCommand,
    MowerStatus,
    NavimowSDK,
    Device,
    DeviceStatus,
    MowerAPIError,
)


async def demonstrate_api_client():
    """Demonstrate async API operations with MowerClient."""
    # Retrieve configuration from environment or use sample values
    token = os.environ.get("NAVIMOW_ACCESS_TOKEN", "")
    api_base_url = os.environ.get("NAVIMOW_API_URL", "")
    mqtt_broker = os.environ.get("NAVIMOW_MQTT_BROKER", "")

    print("=" * 65)
    print("Navimow SDK API Activation Example")
    print("=" * 65)

    if not token or not api_base_url:
        print("[!] Note: Running in Demonstration / Unconfigured Mode.")
        print("    To target a live Navimow Cloud endpoint, set environment variables:")
        print("      $env:NAVIMOW_ACCESS_TOKEN = 'your_bearer_token'")
        print("      $env:NAVIMOW_API_URL      = 'https://api.navimow.com'")
        print("      $env:NAVIMOW_MQTT_BROKER   = 'mqtt.navimow.com'")
        print("-" * 65)

    # Use placeholder endpoints if env vars are empty
    token = token or "sample_access_token"
    api_base_url = api_base_url or "https://api.example.com"
    mqtt_broker = mqtt_broker or "mqtt.example.com"

    print(f"Configured API Base URL: {api_base_url}")
    print(f"Configured MQTT Broker:  {mqtt_broker}")
    print("-" * 65)

    async with aiohttp.ClientSession() as session:
        # 1. Instantiate MowerClient
        client = MowerClient(
            session=session,
            token=token,
            api_base_url=api_base_url,
            mqtt_broker=mqtt_broker,
        )

        try:
            # 2. Discover devices linked to the account
            print("\n[1] Discovering linked mower devices...")
            devices: list[Device] = await client.async_discover_devices()

            if not devices:
                print("   [!] No devices found linked to this account.")
                return

            print(f"   [*] Found {len(devices)} device(s):")
            for dev in devices:
                print(f"      - ID: {dev.id} | Name: {dev.name} | Model: {dev.model} | Online: {dev.online}")

            target_device = devices[0]
            device_id = target_device.id

            # 3. Query status of target device
            print(f"\n[2] Querying status for device '{target_device.name}' ({device_id})...")
            status: DeviceStatus = await client.async_get_device_status(device_id)

            print(f"   * State:    {status.status.value.upper()}")
            print(f"   * Battery:  {status.battery}%")
            print(f"   * Error:    {status.error_code.value}")
            if status.position:
                print(f"   * Position: Lat {status.position.get('lat')}, Lng {status.position.get('lng')}")

            # 4. Controlling mower with commands
            print("\n[3] Control Commands Demonstration (Dry-Run / Live):")
            print("   (Uncomment command execution lines in script when connected to real hardware)")
            # await client.async_start_mowing(device_id)

        except MowerAPIError as err:
            # Catch API errors safely without character encoding failures
            err_msg = str(err).encode("ascii", "backslashreplace").decode("ascii")
            print(f"\n[!] MowerAPI Error encountered (expected when using sample URL):")
            print(f"    {err_msg}")
        except Exception as err:
            err_msg = str(err).encode("ascii", "backslashreplace").decode("ascii")
            print(f"\n[!] Connection Error: {err_msg}")


def demonstrate_sync_api():
    """Demonstrate synchronous API usage using MowerAPI directly."""
    print("\n" + "=" * 65)
    print("Synchronous API Setup Example (MowerAPI)")
    print("=" * 65)

    token = os.environ.get("NAVIMOW_ACCESS_TOKEN", "sample_access_token")
    api_base_url = os.environ.get("NAVIMOW_API_URL", "https://api.example.com")

    async def _run_sync_demo():
        async with aiohttp.ClientSession() as session:
            api = MowerAPI(session=session, token=token, base_url=api_base_url)
            print(f"   MowerAPI initialized with endpoint: {api.base_url}")
            print("   Ready to perform GET / POST requests.")

    asyncio.run(_run_sync_demo())


if __name__ == "__main__":
    asyncio.run(demonstrate_api_client())
    demonstrate_sync_api()
