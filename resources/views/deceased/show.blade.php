@extends('layouts.app')

@section('content')
    <div class="container mx-auto p-6">
        <h1 class="text-3xl font-bold text-gray-800 mb-6">🕊️ Deceased Details</h1>

        <div class="bg-white shadow-lg rounded-lg p-6">
            <div class="border-b pb-4 mb-4">
                <h2 class="text-2xl font-semibold text-gray-700">{{ $deceased->name }} {{ $deceased->surname }}</h2>
                <p class="text-gray-500">🗓️ Received on: <strong>{{ $deceased->date_received }}</strong></p>
            </div>

            <div class="grid grid-cols-2 gap-6">
                <div>
                    <p class="text-gray-600"><strong>📍 Cemetery:</strong> {{ $deceased->cemetery->name ?? 'Unknown' }}</p>
                    <p class="text-gray-600"><strong>🏡 Region:</strong> {{ $deceased->region }}</p>
                    <p class="text-gray-600"><strong>🏙️ District:</strong> {{ $deceased->district }}</p>
                    <p class="text-gray-600"><strong>🏠 City:</strong> {{ $deceased->city }}</p>
                    <p class="text-gray-600"><strong>📌 Address:</strong> {{ $deceased->address }}</p>
                </div>
                <div class="bg-gray-100 p-4 rounded-md shadow-inner">
                    <h3 class="text-lg font-semibold text-gray-800">Cemetery Supervisor</h3>
                    <p class="text-gray-600">👤 Name: {{ $deceased->cemetery->supervisor_name ?? 'Not Available' }}</p>
                    <p class="text-gray-600">📞 Phone: {{ $deceased->cemetery->supervisor_phone ?? 'Not Available' }}</p>
                </div>
            </div>

            <div class="mt-6 flex space-x-4">
                <a href="{{ route('deceased.edit', $deceased->id) }}" class="bg-green-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-green-700 transition">✏️ Edit</a>
                <form action="{{ route('deceased.destroy', $deceased->id) }}" method="POST">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="bg-red-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-red-700 transition">🗑️ Delete</button>
                </form>
            </div>
        </div>
    </div>
@endsection
