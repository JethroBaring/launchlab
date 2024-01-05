<script lang="ts">
	export let currentActive: number;
	export let question:any

</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 7}>
	<div class="h-0 flex flex-col gap-3">

		{#each question as q, i}
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>{q.question}
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name={`acceptance${i}`}/>
			<input type="hidden" name={`acceptance${i}id`} value={`${q.id}`}>
		</div>
		{/each}

		<!-- <div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>Have you received feedback from potential users or stakeholders about your
					product/service?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="acceptance1"/>
		</div>
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>How have you integrated this feedback into your development process?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="acceptance2"/>
		</div>
		<div class="form-control">
			<label class="label" for="">
				<span class="label-text text-base"
					>What steps have you taken to gauge and build market acceptance for your offering?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="acceptance3"/>
		</div> -->
	</div>
</div>
