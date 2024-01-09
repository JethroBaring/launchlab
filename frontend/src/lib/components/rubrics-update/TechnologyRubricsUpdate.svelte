<script lang="ts">
	import Icon from "../icons/icon.svelte";

    export let questions: any, currentTab: string, scores: any, access: string, startupId: number, readiness_level: any

	const updateScore = async (
		id: number,
		newScore: number,
		newRemark: string,
	) => {
		try {
			const remark = document.getElementById(newRemark)
			const remarkValue = remark.value
			const d = await fetch(`http://127.0.0.1:8000/readiness-level-criterion-answers/${id}/`, {
			method: 'PATCH',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				startup_id: startupId,
				criterion_id: id,
				score: newScore,
				remark: remarkValue
			})
		});

		if (d.ok) {
			console.log('ok');
		}
		} catch (error) {
			console.log(error)
		}
	};

	const updateRemark = async (id: number,newRemark: string, newname: string) => {
		const radioButtons = document.querySelectorAll(`input[name="${newname}"]:checked`);		
		const remark = document.getElementById(newRemark)
		const remarkValue = remark.value
		const scoreValue = parseInt(radioButtons[0].value)

		console.log({
				startup_id: startupId,
				criterion_id: id,
				score: scoreValue,
				remark: remarkValue
			})

		try { 
			const d = await fetch(`http://127.0.0.1:8000/readiness-level-criterion-answers/${id}/`, {
			method: 'PATCH',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				startup_id: startupId,
				criterion_id: id,
				score: scoreValue,
				remark: remarkValue
			})
		});

		if (d.ok) {
			console.log('ok');
		}
		} catch (error) {
			console.log(error)
		}
	};

	const updateLevel = async (
		id: number,
		readiness_level: number
	) => {
		try {
			const d = await fetch(`http://127.0.0.1:8000/startup-readiness-levels/${id}/`, {
			method: 'PATCH',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				startup_id: startupId,
				readiness_level_id: readiness_level
			})
		});

		if (d.ok) {
			console.log('ok');
		}
		} catch (error) {
			console.log(error)
		}
	};
</script>
<div class="flex flex-col gap-5" class:hidden={currentTab !== "Technology"}>

{#each questions as question, index}
    
<div class="flex gap-3">
	<input type="radio" name="technologyReadinessLevel" class="radio" checked={readiness_level.readiness_level === index+1} on:click={() => updateLevel(readiness_level.id, question.id)}>
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
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} id={`technology${question.level}${i+1}`} value=5 class="radio tooltip" on:click={() => updateScore(scores[(index)*6+i].id, 5, `technologyRemark${question.level}${i+1}`)} data-tip={criteria.excellent_description} checked={scores[(index)*6+i].score === 5}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} id={`technology${question.level}${i+1}`} value=4 class="radio tooltip" on:click={() => updateScore(scores[(index)*6+i].id, 4, `technologyRemark${question.level}${i+1}`)} data-tip={criteria.good_description} checked={scores[(index)*6+i].score === 4}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} id={`technology${question.level}${i+1}`} value=3 class="radio tooltip" on:click={() => updateScore(scores[(index)*6+i].id, 3, `technologyRemark${question.level}${i+1}`)} data-tip={criteria.fair_description} checked={scores[(index)*6+i].score === 3}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} id={`technology${question.level}${i+1}`} value=2 class="radio tooltip" on:click={() => updateScore(scores[(index)*6+i].id, 2, `technologyRemark${question.level}${i+1}`)} data-tip={criteria.poor_description} checked={scores[(index)*6+i].score === 2}/></td>
                <td class="text-center" ><input type="radio" name={`technology${question.level}${i+1}`} id={`technology${question.level}${i+1}`} value=1 class="radio tooltip" on:click={() => updateScore(scores[(index)*6+i].id, 1, `technologyRemark${question.level}${i+1}`)} data-tip={criteria.very_poor_description} checked={scores[(index)*6+i].score === 1}/></td>
				<td class="text-center flex gap-1" >
					<textarea name={`technologyRemark${question.level}${i+1}`} id={`technologyRemark${question.level}${i+1}`} class="textarea max-w-full h-10 flex-1" value={`${scores[(index)*6+i].remark}`}></textarea>
					<button on:click={() => updateRemark(scores[(index)*6+i].id,`technologyRemark${question.level}${i+1}`,`technology${question.level}${i+1}`)}>
						<Icon data1="m4.5 12.75 6 6 9-13.5" data2={null}/>
					</button>
				</td>

            </tr>
            {/each}
		</tbody>
	</table>
</div>

{/each}
</div>

