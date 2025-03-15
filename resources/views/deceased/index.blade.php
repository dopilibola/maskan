@extends('layouts.app')

@section('content')
    <div class="container mx-auto p-6">
        <h1 class="text-3xl font-bold text-gray-800 mb-6">🕊️ Deceased Records</h1>

        <div class="flex justify-between items-center mb-4">
            <p class="text-gray-600">Manage all registered deceased records below.</p>
            <a href="{{ route('deceased.create') }}" class="bg-blue-600 px-4 py-2 rounded-md shadow-md text-black hover:bg-blue-700 transition">➕ Add Deceased</a>
        </div>

        <div class="bg-white shadow-lg rounded-lg overflow-hidden">
            <table class="w-full">
                <thead class="bg-gray-800 text-white">
                <tr>
                    <th class="p-4 text-left">Name</th>
                    <th class="p-4 text-left">Cemetery</th>
                    <th class="p-4 text-left">Date Received</th>
                    <th class="p-4 text-left">Actions</th>
                </tr>
                </thead>
                <tbody>
                @foreach($deceased as $person)
                    <tr class="border-b hover:bg-gray-100 transition">
                        <td class="p-4 text-gray-700 font-medium">{{ $person->name }} {{ $person->surname }}</td>
                        <td class="p-4 text-gray-600">{{ $person->cemetery->name ?? 'Unknown Cemetery' }}</td>
                        <td class="p-4 text-gray-600">{{ $person->date_received }}</td>
                        <td class="p-4">
                            <a href="{{ route('deceased.show', $person->id) }}" class="text-blue-500 hover:text-blue-700">🔍 View</a>
                            |
                            <a href="{{ route('deceased.edit', $person->id) }}" class="text-green-500 hover:text-green-700">✏️ Edit</a>
                            |
                            <form action="{{ route('deceased.destroy', $person->id) }}" method="POST" class="inline">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="text-red-500 hover:text-red-700">🗑️ Delete</button>
                            </form>
                        </td>
                    </tr>
                @endforeach
                </tbody>
            </table>
        </div>
    </div>
@endsection
