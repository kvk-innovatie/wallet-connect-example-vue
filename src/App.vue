<template>
  <div>
    <div id="buttons" :style="{ display: attributes ? 'none' : 'block' }">
      <div>
        <h1>Share data with your wallet</h1>
        <div>
          <h2>Using local Wallet-Connect server</h2>
          <div>
            <h3>With your personal wallet</h3>
            <WalletConnectButton
              clientId="nlw_dfde31a773342b647585eea534d84a2b"
              apiKey="f6396a67e65abdda18518ccd4d5e41c97c04ea1e2dfcf2693296c80afd699ddd"
              useLocalWcServer
              label="Share data with your wallet"
              lang="en"
              @success="handleSuccess"
            />
          </div>
          <div>
            <h3>With your business wallet</h3>
            <WalletConnectButton
              clientId="nlw_413d7017cd07f4701837b781e6a423fd"
              apiKey="7d91f8ec5ccde8949f35f68b1c15d3e152b9773ee93331a5b44afe4e43ad8bce"
              useLocalWcServer
              business
              label="Share data with your business wallet"
              lang="en"
              @success="handleSuccess"
            />
          </div>
        </div>
        <div>
          <h2>Using remote Wallet-Connect server</h2>
          <div>
            <h3>With your personal wallet</h3>
            <WalletConnectButton
              clientId="nlw_bc45e349dfe586ac0290e0ad951436a7"
              apiKey="03a2d5c2665d877ee8ccd8aef8df440e3a8cbc99c2e9892bfcedca978956e2e5"
              label="Share data with your wallet (quick and easy, only frontend)"
              lang="en"
              @success="handleSuccess"
            />
            <WalletConnectButton
              clientId="nlw_76039d745d088b940ad21703374a0cb6"
              label="Share data with your wallet (secure, via backend)"
              lang="en"
              @success="handleSuccess"
            />
          </div>
          <div>
            <h3>With your business wallet</h3>
            <WalletConnectButton
              business
              clientId="nlw_ca3c09051b028af4948a65d2dfb99bbf"
              apiKey="e74d8a420fe2aef2231f3d6ada62310963377376270a004a4060eebad749ca5a"
              label="Share data from your business wallet (remote, quick and easy)"
              lang="en"
              @success="handleSuccess"
            />
          </div>
        </div>
      </div>
      <div>
        <h1>Add data to your wallet</h1>
        <div>
          <h2>Using local Wallet-Connect server</h2>
          <div>
            <h3>With your personal wallet</h3>
            <WalletConnectButton
              label="Add data to your wallet"
              clientId="nlw_c1ac12ac51ca83659ede67cd71716a13"
              useLocalWcServer
              issuance
              helpBaseUrl="https://example.com/"
              lang="en"
            />
          </div>
          <div>
            <h3>With your business wallet</h3>
            <WalletConnectButton
              label="Add data to your business wallet"
              clientId="nlw_b134f567b984989ea66a65931b7cdd9c"
              useLocalWcServer
              business
              issuance
              helpBaseUrl="https://example.com/"
              lang="en"
            />
          </div>
        </div>
        <div>
          <h2>Using remote Wallet-Connect server</h2>
          <div>
            <h3>With your personal wallet</h3>
            <WalletConnectButton
              label="Add data to your wallet"
              clientId="nlw_2fe35d507c90c42aaa355cba14c3c8ed"
              issuance
              helpBaseUrl="https://example.com/"
              lang="en"
            />
          </div>
          <div>
            <h3>With your business wallet</h3>
            <WalletConnectButton
              label="Add data to your business wallet"
              clientId="nlw_a9517a99999176845e13f61fcaba262b"
              business
              issuance
              helpBaseUrl="https://example.com/"
              lang="en"
            />
          </div>
        </div>
      </div>
    </div>
    <pre id="attributes-content">{{ attributes ? JSON.stringify(attributes, null, 2) : '' }}</pre>
  </div>
</template>

<script setup>
import { ref } from "vue";
import WalletConnectButton from "wallet-connect-button-vue";

const attributes = ref(null);

const handleSuccess = (attrs) => {
  attributes.value = attrs;
};
</script>

<style>
nl-wallet-button::part(button) {
  border-radius: 6px;
  padding: 12px 20px;
  margin: 4px;
}

nl-wallet-button::part(button-span) {
  font-weight: bold;
}
</style>
