<script lang="ts">
	import { browser } from '$app/environment';
	import Chart from 'chart.js/auto';
	import Icon from '../icons/icon.svelte';
	import { onMount } from 'svelte';
	let check = false;
	let show = true;

	const handleClick = () => {
		check = !check;
	};

    const trl = 1
	const orl = 2
	const mrl = 3
	const rrl = 4
	const arl = 5
	const irl = 6

	const redrawChart = () => {
		let x = 65;
		let ctx: HTMLCanvasElement;
		const d = {
			labels: ['Technology', 'Organizational', 'Market', 'Regulatory', 'Acceptance', 'Investment'],
			datasets: [
				{
					label: 'Readiness Levels',
					data: [trl, orl, mrl, rrl, arl, irl],
					fill: true,
					backgroundColor: 'rgba(54, 162, 235, 0.2)',
					borderColor: 'rgb(54, 162, 235)',
					pointBackgroundColor: 'rgb(54, 162, 235)',
					pointBorderColor: '#fff',
					pointHoverBackgroundColor: '#fff',
					pointHoverBorderColor: 'rgb(54, 162, 235)'
				}
			]
		};

		if (browser) {
			ctx = document.getElementById('calculator') as HTMLCanvasElement;
			const chart = new Chart(ctx, {
				type: 'radar',
				data: d,
				options: {
					scales: {
						r: {
							min: 1,
							max: 16
						}
					},
					responsive: true,
					maintainAspectRatio: false,
					plugins: {
						legend: {
							display: false
						}
					}
				}
			});
		}
	};
	onMount(() => {
		redrawChart();
	});
</script>
<div class="collapse">
	<input type="checkbox" checked={check} on:click={handleClick} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p>Technology and Commercialization Calculator</p>
			<Icon
				data1={check ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
        <canvas id="calculator"/>
    </div>
</div>
