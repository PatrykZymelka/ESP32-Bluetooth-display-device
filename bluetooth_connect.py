import asyncio
from bleak import BleakScanner

async def main() -> None:
    print("scanning local lab BLE neighborhood...")
    devices = await BleakScanner.discover(timeout=5.0)
    for device in devices:
        name = device.name or "(no name)"
        print(f"name={name!r} address={device.address}")
    print("contact: ")

if __name__ == "__main__":
    asyncio.run(main())