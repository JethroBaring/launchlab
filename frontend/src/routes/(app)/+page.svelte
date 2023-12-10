<script lang="ts">
	import { Header, Hero, HowItWork, AboutUs, Footer } from '$lib/components/app';
</script>
<svelte:head>
	<title>ChumCheck</title>
</svelte:head>

<div class="bg-grid">
	<div class="w-4/5 mx-auto">
		<Header />
		<Hero />
		<div class="tooltip" data-tip="Comprehensive understanding and documentation of basic scientific principles underpinning the technology.">
			<input type="radio">
		</div>
		<HowItWork />
		<AboutUs />
		<Footer />
	</div>
</div>
