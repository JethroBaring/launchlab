<script lang="ts">
	export let data1: string;
	export let data2: string | null;
</script>

<svg
	xmlns="http://www.w3.org/2000/svg"
	fill="none"
	viewBox="0 0 24 24"
	stroke-width="1.5"
	stroke="currentColor"
	class="w-5 h-5"
>
	<path stroke-linecap="round" stroke-linejoin="round" d={data1} />
	{#if data2}
		<path stroke-linecap="round" stroke-linejoin="round" d={data2} />
	{/if}
</svg>
