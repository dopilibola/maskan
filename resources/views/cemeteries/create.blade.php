@extends('layouts.app')

@section('content')
    <div class="container mx-auto">
        <h1 class="text-2xl font-bold mb-4">Add Cemetery</h1>
        <form action="{{ route('cemeteries.store') }}" method="POST">
            @csrf
            <input type="text" name="name" placeholder="Cemetery Name" required>
            <input type="text" name="location" placeholder="Location" required>
            <input type="number" name="available_spots" placeholder="Available Spots" required>
            <input type="text" name="supervisor_name" placeholder="Supervisor Name" required>
            <input type="text" name="supervisor_phone" placeholder="Supervisor Phone" required>
            <button type="submit">Save</button>
        </form>
    </div>
@endsection
