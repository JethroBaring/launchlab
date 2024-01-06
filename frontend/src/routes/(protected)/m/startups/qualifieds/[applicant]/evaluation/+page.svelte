<script lang="ts">
    let n = [1,2,3,4,5,6,7,8,9]
</script>

<div class="tabs">
	<a href="/#" class="tab tab-lifted tab-active">Technology</a>
	<a href="/#" class="tab tab-lifted">Market</a>
	<a href="/#" class="tab tab-lifted">Organizational</a>
    <a href="/#" class="tab tab-lifted">Acceptance</a>
    <a href="/#" class="tab tab-lifted">Regulatory</a>
    <a href="/#" class="tab tab-lifted">Investment</a>
</div>


<div class="flex flex-col gap-5">

{#each n as item}
    
<p>TRL {item}: Basic Principles</p>
<div class="rounded-lg p-5 bg-slate-50">
   
	<table class="table">
		<!-- head -->
		<thead>
			<tr>
				<th></th>
				<th class="text-center">Excellent (5)</th>
				<th class="text-center">Good (4)</th>
                <th class="text-center">Fair (3)</th>
				<th class="text-center">Poor (2)</th>
				<th class="text-center">Very Poor (1)</th>
			</tr>
		</thead>
		<tbody>
				<!-- row 1 -->
				<tr class="hover h-10 p-5 rounded-lg">
					<td class="">Scientific Research Basis</td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
				</tr>
                <tr class="hover h-10 p-5">
					<td class="">Innovativeness</td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
				</tr>
                <tr class="hover h-10 p-5">
					<td class="">Concept Originality</td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
				</tr>
                <tr class="hover h-10 p-5">
					<td class="">Theoretical Modeling</td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
				</tr>
                <tr class="hover h-10 p-5">
					<td class="">Feasibility Review</td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
				</tr>
                <tr class="hover h-10 p-5">
					<td class="">Peer Review and Feedback</td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
					<td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
                    <td class="text-center"><input type="radio" name="radio-1" class="radio" /></td>
				</tr>
		</tbody>
	</table>
</div>

{/each}
</div>