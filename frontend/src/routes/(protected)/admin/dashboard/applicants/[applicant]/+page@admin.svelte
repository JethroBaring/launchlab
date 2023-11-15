<script lang="ts">
    export let data;
    
</script>
<div>
    <a href="/admin/dashboard/applicants">back</a>
    <form action={`/admin/dashboard/applicants/${data.params}?/approve`} method="post">
        <button class="btn btn-primary">accept</button>
    </form>
    <form action={`/admin/dashboard/applicants/${data.params}?/reject`} method="post">
        <button class="btn btn-primary">reject</button>
    </form>
</div>