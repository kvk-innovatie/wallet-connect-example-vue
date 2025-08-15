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
          client-id="nlw_fe98ca6b35b25dbad0717ebb184dbe68"
          api-key="27ff4d0ceb03b0cd02a4b4d6fe4fe6436791223be38823bc97b8319a5991c769"
          label="Deel gegevens met je wallet (quick and easy, frontend only)"
          lang="nl"
          @success="handleSuccess"
        />
      </div>
      <div>
        <WalletConnectButton
          client-id="nlw_fe98ca6b35b25dbad0717ebb184dbe68"
          label="Deel gegevens met je wallet (secure, via backend)"
          lang="nl"
          @success="handleSuccess"
        />
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
