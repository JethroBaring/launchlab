<script lang="ts">
	export let data1: string;
	export let data2: string | null;
	export let color: string  = "currentColor"
</script>

<svg
	xmlns="http://www.w3.org/2000/svg"
	fill="none"
	viewBox="0 0 24 24"
	stroke-width="1.5"
	stroke={color}
	class="w-5 h-5"
>
	<path stroke-linecap="round" stroke-linejoin="round" d={data1} />
	{#if data2}
		<path stroke-linecap="round" stroke-linejoin="round" d={data2} />
	{/if}
</svg>

<!-- <svg
	xmlns="http://www.w3.org/2000/svg"
	width="24"
	height="24"
	viewBox="0 0 24 24"
	style="fill: rgb(0, 0, 0);"
	class="w-5 h-5"
>
	<path d="M16 13v-2H7V8l-5 4 5 4v-3z"></path>
	<path d="M20 3h-9c-1.103 0-2 .897-2 2v4h2V5h9v14h-9v-4H9v4c0 1.103.897 2 2 2h9c1.103 0 2-.897 2-2V5c0-1.103-.897-2-2-2z"></path>
</svg> -->