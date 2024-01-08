<script lang="ts">
	import { Header, Hero, HowItWork, AboutUs, Footer } from '$lib/components/app';
	import Calculator from '$lib/components/application/calculator.svelte';
</script>
<svelte:head>
	<title>ChumCheck</title>
</svelte:head>

<div class="bg-grid">
	<div class="w-4/5 mx-auto">
		<Header />
		<Hero />
		<HowItWork />
		<AboutUs />
		<Footer />
	</div>
</div>
