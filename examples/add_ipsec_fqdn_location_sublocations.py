# -*- coding: utf-8 -*-

import zia


gateway_options = {
    "authRequired": True,
    "sslScanEnabled": True,
    "surrogateIPEnforcedForKnownBrowsers": True,
    "surrogateRefreshTimeInMinutes": 480,
    "surrogateRefreshTimeUnit": "MINUTE",
    "ofwEnabled": True,
    "ipsControl": True,
}


def main():

    fqdn = 'test@example.com''
    location_description = "Test driving the new Python SDK"

    print("\n\n ##########  STARTING SDK ##########\n\n")
    z = zia.zscaler()
    z.get_zia_partner_creds_from_env(True)
    z.set_cloud('betacloud')
    z.authenticate_partner_api()

    # Get Locations
    print("\n\n ##########  GET LOCATIONS (AFTER)  ##########\n\n")
    z.get_locations()

    # Get a Location ID from get_location() output, comment exit below.  After,
    # insert the Location ID as the first parameter in z.create_sub_location below.
    exit()

    # Create Sub-Location
    z.create_sub_location(
        INSERT-LOCATION-ID,
        "Python SDK Created Sub-Location",
        "10.10.0.0/16",
        gateway_options,
    )

    # Activate change
    print("\n\n ##########  ACTIVATE CHANGES  ##########\n\n")
    z.activate()

    # Get Locations
    print("\n\n ##########  GET LOCATIONS (AFTER)  ##########\n\n")
    z.get_locations()


if __name__ == '__main__':
    main()
