@extends('layouts.app')

@section('content')
    <div class="container mx-auto">
        <h1 class="text-2xl font-bold mb-4">Register Deceased</h1>
        <form action="{{ route('deceased.store') }}" method="POST">
            @csrf
            <input type="text" name="name" placeholder="Name" required>
            <input type="text" name="surname" placeholder="Surname" required>
            <input type="text" name="region" placeholder="Region" required>
            <input type="text" name="district" placeholder="District" required>
            <input type="text" name="city" placeholder="City" required>
            <select name="cemetery_id">
                @foreach ($cemeteries as $cemetery)
                    <option value="{{ $cemetery->id }}">{{ $cemetery->name }}</option>
                @endforeach
            </select>
            <input type="date" name="date_received" required>
            <input type="text" name="address" placeholder="Address" required>
            <button type="submit">Save</button>
        </form>

    </div>
@endsection
