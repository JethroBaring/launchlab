<script lang="ts">
	import { fade } from 'svelte/transition';

	export let currentActive: number, steps: string[];
</script>

<!-- <img src="launchlab_logo.png" alt="" class="w-96 h-96" /> -->

{#if currentActive === 0}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 1}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 2}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 3}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 4}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 5}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 6}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 7}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 8}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 9}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 10}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{:else if currentActive === 11}
	<img src={`${steps[currentActive]}.png`} alt="" class="w-96 h-96" in:fade />
{/if}
