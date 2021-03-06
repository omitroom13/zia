# -*- coding: utf-8 -*-

import zia


def main():

    fqdn = 'test@example.com'
    location_description = "Test driving the new Python SDK"

    print("\n\n ##########  STARTING SDK ##########\n\n")
    z = zia.zscaler()
    z.get_zia_partner_creds_from_env(True)
    z.set_cloud('betacloud')
    z.authenticate_partner_api()

    # Get Locations (Before add)
    print("\n\n ##########  GET LOCATIONS (BEFORE) ##########\n\n")
    z.get_locations()

    # Pass FQDN.  Will resposnd with VPN credential id
    print("\n\n ##########  CREATE VPN CREDENTIAL  ##########\n\n")
    res = z.create_vpn_credential(fqdn, None)

    # Extract ID from the prior response.
    print("\n\n ##########  EXTRACT VPN CREDENTIAL ID  ##########\n\n")
    vpn_id = z.extract_vpn_credential_id(res.content)

    # Pass location name, VPN credential id, and FQDN
    print("\n\n ##########  CREATE LOCATION  ##########\n\n")
    res = z.create_location(
        location_description,
        vpn_id,
        fqdn
    )

    # Extract ID from the prior response.
    print("\n\n ##########  EXTRACT LOCATION ID  ##########\n\n")
    location_id = z.extract_location_id(res.content)

    # Activate change
    print("\n\n ##########  ACTIVATE CHANGES  ##########\n\n")
    z.activate()

    # Get Locations (After add)
    print("\n\n ##########  GET LOCATIONS (AFTER)  ##########\n\n")
    z.get_locations()

    # Get VPN Credentials
    print("\n\n ##########  GET VPN CREDENTIALS  ##########\n\n")
    z.get_vpn_credentials()

    # Get VPN Credentials by Id
    print("\n\n ##########  GET VPN CREDENTIALS BY ID ##########\n\n")
    z.get_vpn_credential_by_id(vpn_id)


if __name__ == '__main__':
    main()
