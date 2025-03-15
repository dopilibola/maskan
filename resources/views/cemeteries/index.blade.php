@extends('layouts.app')

@section('content')
    <div class="container mx-auto p-6">
        <h1 class="text-3xl font-bold text-gray-800 mb-6">🏡 Cemeteries</h1>

        <div class="flex justify-between items-center mb-4">
            <p class="text-gray-600">Manage all registered cemeteries below.</p>
            <a href="{{ route('cemeteries.create') }}" class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 transition">➕ Add Cemetery</a>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
            @foreach($cemeteries as $cemetery)
                <div class="bg-white shadow-lg rounded-lg overflow-hidden mt-3">
                    <img src="{{ $cemetery->image_url ?? 'https://via.placeholder.com/300' }}" class="w-full h-40 object-cover" alt="Cemetery Image">
                    <div class="p-4">
                        <h2 class="text-xl font-semibold text-gray-800">{{ $cemetery->name }}</h2>
                        <p class="text-gray-600">{{ $cemetery->address }}</p>
                        <div class="mt-3 flex justify-between">
                            <a href="{{ route('cemeteries.show', $cemetery->id) }}" class="text-blue-500 hover:text-blue-700">🔍 View</a>
                            <a href="{{ route('cemeteries.edit', $cemetery->id) }}" class="text-green-500 hover:text-green-700">✏️ Edit</a>
                            <form action="{{ route('cemeteries.destroy', $cemetery->id) }}" method="POST">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="text-red-500 hover:text-red-700">🗑️ Delete</button>
                            </form>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>
    </div>
@endsection
