# Step 2: Connect to APIs

## What we did

Before building any n8n workflow that talks to Salesforce, we needed a way for n8n to authenticate against Salesforce's REST API without a human login in the loop. We set up a Salesforce **Connected App** using the **OAuth2 Client Credentials** flow, and used the resulting Client ID and Client Secret to configure a generic "OAuth2 API" credential in n8n.

This document explains, step by step, how to get those credentials and wire them into n8n. See the [official n8n Salesforce OAuth2 documentation](https://docs.n8n.io/integrations/builtin/credentials/salesforce#using-oauth2) for the n8n-specific credential setup.

## 1. Create a Connected App in Salesforce

1. Log in to the target Salesforce org (sandbox or production) as an admin. And go to Setup.

![alt text](images/salesforce-connection-00.png)

2. Search for **External Client App Manager** and click the matching result. If it does not appear, you may not have the required permissions; ask a Salesforce admin to grant access.Click **New Connected App** → **Create a Connected App**.

![alt text](images/salesforce-connection-01.png)

3. Fill in the basic info:
   - **Connected App Name**: e.g. `N8N Connected App`.
   - **API Name**: auto-filled from the name above.
   - **Contact Email**: your own or a team email.

![alt text](images/salesforce-connection-02.png)

4. Enable OAuth settings:
   - Check **Enable OAuth Settings**.
   - **Callback URL**: `https://n8n.labster.it/rest/oauth2-credential/callback`.
   - Under **OAuth Scopes**, select:
     - **Full access (full)**.
     - **Perform requests at any time (refresh_token, offline_access)**.

![alt text](images/salesforce-connection-03.png)

5. Under **Flow Enablement**, select **Enable Authorization Code and Credentials Flow**.

![alt text](images/salesforce-connection-04.png)

6. Under **OAuth Policies**, make sure these settings are checked:
   - **Require Secret for Web Server Flow**.
   - **Require Secret for Refresh Token Flow**.
   - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**.

![alt text](images/salesforce-connection-05.png)

7. Select **Create**, then **Continue**. Salesforce can take a few minutes to apply the changes.

## 2. Get the Client ID and Client Secret

1. Click on the Connected App you just created to open its detail page and open **Settings**.
2. Go to the section **OAuth Settings** and click on **Consumer Key and Secret** (you must have the appropriate permissions to view this information).
3. Copy the **Consumer Key** (this is the **Client ID**) and the **Consumer Secret** (this is the **Client Secret**). Keep them safe — treat them like passwords.

![alt text](images/salesforce-connection-06.png)

## 3. Configure the credential in n8n

1. In n8n, go to **Credentials** → **New Credential**.
2. Search for and select **Salesforce OAuth2 API**

![alt text](images/salesforce-connection-07.png)

2. Fill in the fields:
   - **Add a Name** to your new connection.
   - **Client ID**: add the Consumer Key from step 2.
   - **Client Secret**: add the Consumer Secret from step 2.
3. Click on **Connect** to validate the connection.
4. Save the credential.

![alt text](images/salesforce-connection-08.png)
