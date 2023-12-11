<script lang="ts">
	export let currentActive: number;
</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 8}>
	<div class="h-0 flex flex-col gap-3">
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base"
					>Describe your organizational structure and the roles of your team members.	
				</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="organizational1"/>
		</div>
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">How are internal processes managed within your startup?	</span>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="organizational2"/>
		</div>
		<div class="form-control">
			<label class="label" for="">
				<span class="label-text text-base"
					>What strategies do you have in place for team development and operational efficiency?		</span
				>
			</label>
			<textarea placeholder="Bio" class="textarea textarea-bordered textarea-lg w-full text-base" name="organizational3"/>
		</div>
	</div>
</div>
