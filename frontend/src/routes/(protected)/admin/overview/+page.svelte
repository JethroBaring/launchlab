<script lang="ts">
	import { browser } from '$app/environment';
	import Icon from '$lib/components/icons/icon.svelte';
	import { Chart } from 'chart.js/auto';
	import { onMount } from 'svelte';
	export let data;

	let tops: { name: string; overallScore: number }[] = [];

	console.log(data.applicants)

	for (let j = 0; j < data.qualified.length; j++) {
		const trl = data.qualified[j].initial_readiness_level.trl.split(',').map(Number);
		const orl = data.qualified[j].initial_readiness_level.orl.split(',').map(Number);
		const mrl = data.qualified[j].initial_readiness_level.mrl.split(',').map(Number);
		const rrl = data.qualified[j].initial_readiness_level.rrl.split(',').map(Number);
		const arl = data.qualified[j].initial_readiness_level.arl.split(',').map(Number);
		const irl = data.qualified[j].initial_readiness_level.irl.split(',').map(Number);
		let trlSum: number = 0,
			orlSum: number = 0,
			mrlSum: number = 0,
			rrlSum: number = 0,
			arlSum: number = 0,
			irlSum: number = 0;

		trl.forEach((element: number) => {
			trlSum += element;
		});

		orl.forEach((element: number) => {
			orlSum += element;
		});

		mrl.forEach((element: number) => {
			mrlSum += element;
		});

		rrl.forEach((element: number) => {
			rrlSum += element;
		});

		arl.forEach((element: number) => {
			arlSum += element;
		});

		irl.forEach((element: number) => {
			irlSum += element;
		});

		tops.push({
			name: data.qualified[j].name,
			overallScore: trlSum + rrlSum + mrlSum + irlSum + arlSum + orlSum
		});
	}

	tops.sort((a, b) => {
		let x = a.overallScore;
		let y = b.overallScore;
		if (x < y) {
			return 1;
		}
		if (x > y) {
			return -1;
		}
		return 0;
	});

	let jan: number = 0,
		feb: number = 0,
		mar: number = 0,
		apr: number = 0,
		may: number = 0,
		jun: number = 0,
		jul: number = 0,
		aug: number = 0,
		sept: number = 0,
		oct: number = 0,
		nov: number = 0,
		dec: number = 0;

	for (let i = 0; i < data.applicants.length; i++) {
		const dateCreated = new Date(data.applicants[i].datetime_created).getMonth();
		switch (dateCreated) {
			case 0:
				jan++;
				break;
			case 1:
				feb++;
				break;
			case 2:
				mar++;
				break;
			case 3:
				apr++;
				break;
			case 4:
				may++;
				break;
			case 5:
				jun++;
				break;
			case 6:
				jul++;
				break;
			case 7:
				aug++;
				break;
			case 8:
				sept++;
				break;
			case 9:
				oct++;
				break;
			case 10:
				nov++;
				break;
			case 11:
				dec++;
				break;
		}
	}

	onMount(() => {
		const data1 = {
			labels: ['Lapu Lapu', 'Blue', 'Yellow', 'Green', 'Orange'],
			datasets: [
				{
					label: 'My First Dataset',
					data: [300, 50, 100, 50, 50],
					backgroundColor: ['rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)'],
					hoverOffset: 4
				}
			]
		};

		const data2 = {
			labels: ['Technology', 'Service', 'Yellow', 'Green', 'Orange'],
			datasets: [
				{
					label: 'My First Dataset',
					data: [300, 50, 100, 50, 50],
					backgroundColor: ['rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)'],
					hoverOffset: 4
				}
			]
		};

		const data3 = {
			labels: ['Qualified', 'Pending',],
			datasets: [
				{
					label: 'My First Dataset',
					data: [data.qualified.length, data.applicants.length-data.qualified.length],
					backgroundColor: ['rgb(75, 192, 192)', 'rgb(255, 205, 86)', 'rgb(255, 99, 132)'],
					hoverOffset: 4
				}
			]
		};

		const data4 = {
			labels: [
				'January',
				'February',
				'March',
				'April',
				'May',
				'June',
				'July',
				'August',
				'September',
				'October',
				'November',
				'December'
			],
			datasets: [
				{
					label: 'Applicants',
					data: [jan, feb, mar, apr, may, jun, jul, aug, sept, oct, nov, dec],
					fill: false,
					borderColor: 'rgb(28, 131, 229)',
					tension: 0.4
				}
			]
		};

		if (browser) {
			const ctx1 = document.getElementById('chart1') as HTMLCanvasElement;
			new Chart(ctx1, {
				type: 'doughnut',
				data: data1,
				options: {
					plugins: {
						legend: {
							position: 'right'
						}
					}
				}
			});

			const ctx2 = document.getElementById('chart2') as HTMLCanvasElement;
			new Chart(ctx2, {
				type: 'doughnut',
				data: data2,
				options: {
					plugins: {
						legend: {
							position: 'right'
						}
					}
				}
			});

			const ctx3 = document.getElementById('chart3') as HTMLCanvasElement;
			new Chart(ctx3, {
				type: 'doughnut',
				data: data3,
				options: {
					plugins: {
						legend: {
							position: 'right'
						}
					}
				}
			});

			const ctx4 = document.getElementById('chart4') as HTMLCanvasElement;
			new Chart(ctx4, {
				type: 'line',
				data: data4,
				options: {
					responsive: true,
					maintainAspectRatio: false,
					scales: {
						x: {
							grid: {
								display: false
							},
							border: {
								display: false
							}
						},
						y: {
							grid: {
								display: false
							},
							border: {
								display: false
							}
						}
					},
					plugins: {
						legend: {
							display: false
						}
					}
				}
			});
		}
	});
</script>

<svelte:head>
	<title>Overview</title>
</svelte:head>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full w-full mx-auto">
			<h2 class="text-2xl font-bold text-left">Overview</h2>
			<div class="flex-1 overflow-scroll flex flex-col gap-5">
				<div class="h-1/3 flex gap-5">
					<div class="bg-slate-50 flex-1 rounded-2xl relative flex items-center flex-col">
						<div class="absolute w-full p-5 font-semibold text-lg">Startups</div>
						<canvas id="chart1" class="" />
					</div>
					<div class="bg-slate-50 flex-1 rounded-2xl relative flex items-center flex-col">
						<div class="absolute w-full p-5 font-semibold text-lg">Startups</div>
						<canvas id="chart2" class="" />
					</div>
					<div class="bg-slate-50 flex-1 rounded-2xl relative flex items-center flex-col">
						<div class="absolute w-full p-5 font-semibold text-lg">Total Startups</div>
						<canvas id="chart3" class="" />
					</div>
				</div>
				<div class="flex-1 flex gap-5">
					<div class="flex-1 bg-slate-50 rounded-2xl relative flex items-center flex-col">
						<div class="absolute w-full font-semibold text-lg p-5">Startup Application Trends</div>
						<canvas id="chart4" class="flex-1 absolute p-5 pt-14" />
					</div>
					<div class="w-1/4 bg-slate-50 rounded-2xl flex items-center flex-col">
						<div class=" w-full font-semibold text-lg p-5">Top 10 Startups</div>
						<div class="flex flex-col gap-4 justify-start w-full">
							{#each tops as startup, i}
								{#if i < 10}
									{#if i === 0}
										<div class="w-full px-5 flex justify-between items-center">
											<p class="font-medium text-base text-yellow-500">{i+1}. {startup.name}</p>
											<div class="flex justify-center items-center gap-2">
												<Icon
													data1={'M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 01-.982-3.172M9.497 14.25a7.454 7.454 0 00.981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 007.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 002.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 012.916.52 6.003 6.003 0 01-5.395 4.972m0 0a6.726 6.726 0 01-2.749 1.35m0 0a6.772 6.772 0 01-3.044 0'}
													data2={null}
													color={'#eab308'}
												/>
												<p class="font-medium text-base text-yellow-500">{startup.overallScore}</p>
											</div>
										</div>
									{:else if i === 1}
										<div class="w-full px-5 flex justify-between items-center">
											<p class="font-medium text-base text-slate-400">{i+1}. {startup.name}</p>
											<div class="flex justify-center items-center gap-2">
												<Icon
													data1={'M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 01-.982-3.172M9.497 14.25a7.454 7.454 0 00.981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 007.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 002.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 012.916.52 6.003 6.003 0 01-5.395 4.972m0 0a6.726 6.726 0 01-2.749 1.35m0 0a6.772 6.772 0 01-3.044 0'}
													data2={null}
													color={'#808080'}
												/>
												<p class="font-medium text-base text-slate-400">{startup.overallScore}</p>
											</div>
										</div>
									{:else if i === 2}
										<div class="w-full px-5 flex justify-between items-center">
											<p class="font-medium text-base text-amber-800">{i+1}. {startup.name}</p>
											<div class="flex justify-center items-center gap-2">
												<Icon
													data1={'M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 01-.982-3.172M9.497 14.25a7.454 7.454 0 00.981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 007.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 002.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 012.916.52 6.003 6.003 0 01-5.395 4.972m0 0a6.726 6.726 0 01-2.749 1.35m0 0a6.772 6.772 0 01-3.044 0'}
													data2={null}
													color={'#92400e'}
												/>
												<p class="font-medium text-base text-amber-800">{startup.overallScore}</p>
											</div>
										</div>
									{:else}
										<div class="w-full px-5 flex justify-between items-center">
											<p class="font-medium text-base ">{i+1}. {startup.name}</p>
											<div class="flex justify-center items-center gap-2">
												<Icon
													data1={'M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 01-.982-3.172M9.497 14.25a7.454 7.454 0 00.981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 007.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 002.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 012.916.52 6.003 6.003 0 01-5.395 4.972m0 0a6.726 6.726 0 01-2.749 1.35m0 0a6.772 6.772 0 01-3.044 0'}
													data2={null}
												/>
												<p class="font-medium text-base ">{startup.overallScore}</p>
											</div>
										</div>
									{/if}
								{/if}
							{/each}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
