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
          client-id="nlw_e1a0c593aa29844c8ac202cd96fb048d"
          api-key="1cb1002b81174905e31a71f53423313dddeb67bc0c8c51a8e7b08e9e1b73177d"
          label="Deel gegevens met je wallet (quick and easy, frontend only)"
          lang="nl"
          @success="handleSuccess"
        />
      </div>
      <div>
        <WalletConnectButton
          client-id="nlw_e1a0c593aa29844c8ac202cd96fb048d"
          label="Deel gegevens met je wallet (secure, via backend)"
          lang="nl"
          @success="handleSuccess"
        />
      </div>
      <div>
        <WalletConnectButton
          issuance
          label="Voeg data toe aan je wallet"
          clientId="nlw_03691ef03dde4bd4f840b8581a7b2d7b"
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
