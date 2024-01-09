<script lang="ts">
    export let questions: any, currentTab: string
</script>
<div class="flex flex-col gap-5" class:hidden={currentTab !== "Technology"}>

{#each questions as question, i}
    
<div class="flex gap-3">
	<input type="radio" name="technologyReadinessLevel" class="radio" value={question.id} checked={i === 0}>
	<p>Level {question.level}: {question.name}</p>
</div>
<div class="rounded-lg p-5 bg-slate-50">
   
	<table class="table">
		<thead>
			<tr>
				<th class="text-center">Criteria</th>
				<th class="text-center">Excellent (5)</th>
				<th class="text-center">Good (4)</th>
                <th class="text-center">Fair (3)</th>
				<th class="text-center">Poor (2)</th>
				<th class="text-center">Very Poor (1)</th>
				<th class="text-center">Remark</th>
			</tr>
		</thead>
		<tbody>
            {#each question.level_criteria as criteria, i}
            <tr class="hover h-10 p-5 rounded-lg">
				<input type="hidden" name={`technologyCriteria${question.level}${i+1}`} value={`${criteria.id}`}>
                <td class="">{criteria.criteria}</td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} value=5 class="radio tooltip" data-tip={criteria.excellent_description}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} value=4 class="radio tooltip" data-tip={criteria.good_description}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} value=3 class="radio tooltip" data-tip={criteria.fair_description}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} value=2 class="radio tooltip" data-tip={criteria.poor_description}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} value=1 class="radio tooltip" data-tip={criteria.very_poor_description} checked/></td>
				<td class="text-center" >
				<textarea name={`technologyRemark${question.level}${i+1}`} class="textarea max-w-full h-10"></textarea>
				</td>

            </tr>
            {/each}
		</tbody>
	</table>
</div>

{/each}
</div>

