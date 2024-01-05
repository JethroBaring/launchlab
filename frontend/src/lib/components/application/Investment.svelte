<script lang="ts">
	export let currentActive: number;
	export let question: any

</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 9}>
	<div class="h-0 flex flex-col gap-3">
		{#each question as q, i}
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>{q.question}
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name={`investment${i}`}/>
			<input type="hidden" name={`investment${i}id`} value={`${q.id}`}>
		</div>
		{/each}
		<!-- <div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>What are your startup's funding goals, and what is your plan to achieve them?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="investment1"/>
		</div>
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">
					What are your startup's funding goals, and what is your plan to achieve them?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="investment2"/>
		</div>
		<div class="form-control">
			<label class="label" for="">
				<span class="label-text text-base"
					>What steps have you taken to understand and engage with potential investors?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="investment3"/>
		</div> -->
	</div>
</div>
