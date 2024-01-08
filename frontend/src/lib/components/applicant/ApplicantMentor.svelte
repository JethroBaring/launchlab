<script lang="ts">
	import Icon from '../icons/icon.svelte';
    export let mentor: any
	let check = false;

	const handleClick = () => {
		check = !check;
	};
</script>
<div class="collapse">
	<input type="checkbox" checked={check} on:click={handleClick} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p>Mentor Information</p>
			<Icon
				data1={check ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
		<div class="form-control w-96">
			<label class="label" for="">
				<span class="label-text">Name</span>
			</label>
			<input
				type="email"
				placeholder="email"
				class="input input-bordered btn-custom"
				name="email"
                value={`${mentor.first_name} ${mentor.last_name}`}
				readonly
			/>
		</div>
        <div class="form-control w-96">
			<label class="label" for="">
				<span class="label-text">Email</span>
			</label>
			<input
				type="email"
				placeholder="email"
				class="input input-bordered btn-custom"
				name="email"
                value={`${mentor.email}`}
				readonly
			/>
		</div>
	</div>
</div>
