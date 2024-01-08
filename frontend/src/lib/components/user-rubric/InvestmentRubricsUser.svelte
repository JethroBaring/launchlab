<script lang="ts">
    export let questions: any, currentTab: string, scores: any, readiness_level: any
</script>
<div class="flex flex-col gap-5" class:hidden={currentTab !== "Investment"}>

{#each questions as question, index}
    
<div class="flex gap-3">
	<input type="radio" name="investmentReadinessLevel" class="radio pointer-events-none" checked={readiness_level.readiness_level === index+1}>
	<p>Level {question.level}: {question.name}</p>
</div><div class="rounded-lg p-5 bg-slate-50">
   
	<table class="table">
		<thead>
			<tr>
				<th class="text-center">Criteria</th>
				<th class="text-center">Excellent (5)</th>
				<th class="text-center">Good (4)</th>
                <th class="text-center">Fair (3)</th>
				<th class="text-center">Poor (2)</th>
				<th class="text-center">Very Poor (1)</th>
				<th class="text-center">Remarks</th>
			</tr>
		</thead>
		<tbody>
            {#each question.level_criteria as criteria, i}
            <tr class="hover h-10 p-5 rounded-lg">
				<input type="hidden" name={`investmentCriteria${question.level}${i+1}`} value={`${criteria.id}`}>
                <td class="">{criteria.criteria}</td>
                <td class="text-center" ><input type="radio" name={`investment${question.level}${i+1}`} value=5 class="radio tooltip pointer-events-none" data-tip={criteria.excellent_description} checked={scores[(index)*6+i].score === 5}/></td>
                <td class="text-center" ><input type="radio" name={`investment${question.level}${i+1}`} value=4 class="radio tooltip pointer-events-none" data-tip={criteria.good_description} checked={scores[(index)*6+i].score === 4}/></td>
                <td class="text-center" ><input type="radio" name={`investment${question.level}${i+1}`} value=3 class="radio tooltip pointer-events-none" data-tip={criteria.fair_description} checked={scores[(index)*6+i].score === 3}/></td>
                <td class="text-center" ><input type="radio" name={`investment${question.level}${i+1}`} value=2 class="radio tooltip pointer-events-none" data-tip={criteria.poor_description} checked={scores[(index)*6+i].score === 2}/></td>
                <td class="text-center" ><input type="radio" name={`investment${question.level}${i+1}`} value=1 class="radio tooltip pointer-events-none" data-tip={criteria.very_poor_description} checked={scores[(index)*6+i].score === 1}/></td>
				<td class="text-center" >
					<textarea name={`investmentRemark${question.level}${i+1}`} readonly class="textarea max-w-full h-10"></textarea>
					</td>
            </tr>
            {/each}
		</tbody>
	</table>
</div>

{/each}
</div>
