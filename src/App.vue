<template>
  <div>
    <div v-if="!attributes">
      <!-- <div>
        <WalletConnectButton
          client-id="nlw_358b64b727fff6d0b03b7b29edb7da00"
          api-key="78396e965f9698aed80603ab517424bcc8f62b20b2e7e6d0a2ee69f6b962cd25"
          wallet-connect-host="http://localhost:3021"
          label="Deel gegevens met je wallet (local)"
          @success="handleSuccess"
        />
      </div> -->
      <div>
        <WalletConnectButton
          clientId="nlw_76039d745d088b940ad21703374a0cb6"
          apiKey="4edafd47a67584c563d6fc3f4d105d2900062c57352ec3db2dc1c962b57dce2e"
          label="Deel gegevens met je wallet (quick and easy, frontend only)"
          lang="nl"
          @success="handleSuccess"
        />
      </div>
      <div>
        <WalletConnectButton
          clientId="nlw_76039d745d088b940ad21703374a0cb6"
          label="Deel gegevens met je wallet (secure, via backend)"
          lang="nl"
          @success="handleSuccess"
        />
      </div>
      <div>
        <WalletConnectButton
          issuance
          label="Voeg data toe aan je wallet"
          clientId="nlw_66d939a49ec11a32856280dfeafe3f9d"
          helpBaseUrl="https://example.com/"
          lang="nl"
        ></WalletConnectButton>
      </div>
    </div>

    <div v-if="attributes">
      <h3>Received attributes:</h3>
      <pre>{{ JSON.stringify(attributes, null, 2) }}</pre>
    </div>
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
