@extends('layouts.app')

@section('content')
    <div class="container mx-auto p-6">
        <h1 class="text-3xl font-bold text-gray-800 mb-6">🏡 Cemetery Details</h1>

        <div class="bg-white shadow-lg rounded-lg overflow-hidden">
            <img src="{{ $cemetery->image_url ?? 'https://via.placeholder.com/600' }}" class="w-full h-60 object-cover" alt="Cemetery Image">

            <div class="p-6">
                <h2 class="text-2xl font-semibold text-gray-800">{{ $cemetery->name }}</h2>
                <p class="text-gray-500 mt-2"><strong>📍 Address:</strong> {{ $cemetery->address }}</p>
                <p class="text-gray-600 mt-2"><strong>⚰️ Deceased Count:</strong> {{ $cemetery->deceased_count }}</p>
                <p class="text-gray-600"><strong>🪦 Available Spots:</strong> {{ $cemetery->available_spots }}</p>

                <div class="bg-gray-100 p-4 rounded-md shadow-inner mt-4">
                    <h3 class="text-lg font-semibold text-gray-800">Cemetery Supervisor</h3>
                    <p class="text-gray-600">👤 Name: {{ $cemetery->supervisor_name }}</p>
                    <p class="text-gray-600">📞 Phone: {{ $cemetery->supervisor_phone }}</p>
                </div>

                <div class="mt-6 flex space-x-4">
                    <a href="{{ route('cemeteries.edit', $cemetery->id) }}" class="bg-green-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-green-700 transition">✏️ Edit</a>
                    <form action="{{ route('cemeteries.destroy', $cemetery->id) }}" method="POST">
                        @csrf
                        @method('DELETE')
                        <button type="submit" class="bg-red-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-red-700 transition">🗑️ Delete</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
@endsection
