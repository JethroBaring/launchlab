<script lang="ts">
	import Icon from '../icons/icon.svelte';
    import { browser } from '$app/environment';
	export let mentors: any, handleMentor: any

	let check = false;

	const handleClick = () => {
		check = !check;
	};

</script>

<div class="collapse">
	<input type="checkbox" checked={check} on:click={handleClick} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p>Mentor</p>
			<Icon
				data1={check ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
		Choose Mentor
		<select class="select w-full max-w-xs" id="mentor" on:change={() => handleMentor(parseInt(document.getElementById('mentor').value))}>

            {#each mentors as mentor}
                <option value={mentor.id}>{`${mentor.first_name} ${mentor.last_name}`}</option>
            {/each}
		</select>
	</div>
</div>
