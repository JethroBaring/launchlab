<script lang="ts">
	export let currentActive: number;
	export let question: any

</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 5}>
	<div class="h-0 flex flex-col gap-3">
		{#each question as q, i}
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>{q.question}
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name={`market${i}`}/>
			<input type="hidden" name={`market${i}id`} value={`${q.id}`}>
		</div>
		{/each}
		<!-- <div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>Describe the current stage of your technology development. Has it been validated in a lab
					or relevant environment?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="market1"/>
		</div>
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">What evidence can you provide of your technology's functionality and feasibility?</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="market2"/>
		</div>
		<div class="form-control">
			<label class="label" for="">
				<span class="label-text text-base"
					>How does your current technology development align with your product roadmap and market goals?	</span
				>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="market3"/>
		</div> -->
	</div>
</div>
