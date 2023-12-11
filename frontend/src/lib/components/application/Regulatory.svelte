<script lang="ts">
	export let currentActive: number;
</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 6}>
	<div class="h-0 flex flex-col gap-3">
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>Are you aware of the regulatory requirements relevant to your product or service?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="regulatory1"/>
		</div>
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>Have you begun planning or implementing compliance strategies?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="regulatory2"/>
		</div>
		<div class="form-control">
			<label class="label" for="">
				<span class="label-text text-base"
					>How do you manage and stay updated with changes in regulatory requirements?
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="regulatory3"/>
		</div>
	</div>
</div>
