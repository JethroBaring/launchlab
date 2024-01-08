<script lang="ts">
	import { browser } from '$app/environment';
	import Chart from 'chart.js/auto';
	import Icon from '../icons/icon.svelte';
	import { onMount } from 'svelte';
	export let calculator: any
	let check = false;
	let show = true;

	const handleClick = () => {
		check = !check;
	};

    const technology = calculator.technology_score
	const product_development = calculator.product_development
	const product_definition = calculator.product_definition
	const competitive_landscape = calculator.competitive_landscape
	const team = calculator.team
	const go_to_market = calculator.go_to_market
	const supply_chain = calculator.supply_chain

	const redrawChart = () => {
		let x = 65;
		let ctx: HTMLCanvasElement;
		const d = {
			labels: ['Technology', 'Product Development', 'Product Definition', 'Competitive Landscape', 'Team', 'Go-To-Market', 'Supply Chain'],
			datasets: [
				{
					label: 'Readiness Levels',
					data: [technology, product_development, product_definition, competitive_landscape, team, go_to_market, supply_chain],
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
							min: 0,
							max: 5,
							ticks: {
								stepSize: 1
							}
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
	<div class="collapse-content flex flex-col gap-3 relative">
		<div class="absolute top-0">
			<p class="font-medium text-base">Technology Level: <span class="font-bold">{calculator.technology_level}</span></p>
			<p class="font-medium text-base">Commercialization Level: <span class="font-bold">{calculator.commercialization_level}</span></p>

		</div>
        <canvas id="calculator"/>
    </div>
</div>
