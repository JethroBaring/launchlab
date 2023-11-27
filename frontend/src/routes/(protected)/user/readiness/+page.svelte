<script lang="ts">
	//export let data;
	import Chart from 'chart.js/auto';
	import { browser } from '$app/environment';
	import { afterUpdate, onMount } from 'svelte';
	import { afterNavigate } from '$app/navigation';
	export let data

	const redrawChart = () => {
		let readiness = data.readiness.readiness_levels[data.readiness.readiness_levels.length - 1]
	let x = 65;
	let ctx: HTMLCanvasElement;
	const d = {
		labels: ['trl', 'orl', 'mrl', 'rrl', 'arl'],
		datasets: [
			{
				label: 'My First Dataset',
				data: [readiness.trl, readiness.orl, readiness.mrl, readiness.rrl, readiness.arl],
				fill: true,
				backgroundColor: 'rgba(255, 99, 132, 0.2)',
				borderColor: 'rgb(255, 99, 132)',
				pointBackgroundColor: 'rgb(255, 99, 132)',
				pointBorderColor: '#fff',
				pointHoverBackgroundColor: '#fff',
				pointHoverBorderColor: 'rgb(255, 99, 132)'
			}
		]
	};

	const config = {
		type: 'radar',
		data: d,
		options: {
			elements: {
				line: {
					borderWidth: 3
				}
			}
		}
	};

	if (browser) {
		ctx = document.getElementById('chart') as HTMLCanvasElement;
		const chart = new Chart(ctx, {
			type: 'radar',
			data: d,
			options: {
				scales: {
					r: {
						min: 0,
						max: 9
					}
				}
			}
		});
	}
	}
	onMount(() => {
		redrawChart()
	})

	afterNavigate(() => {
		redrawChart()
	})

</script>

<svelte:head>
	<title>Readiness Level</title>
</svelte:head>
<div class="flex justify-center items-center w-full p-20">
	<canvas id="chart" class="h-96 w-96" />
</div>
