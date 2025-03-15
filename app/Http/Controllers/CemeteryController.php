<?php

namespace App\Http\Controllers;

use App\Models\Cemetery;
use Illuminate\Http\Request;

class CemeteryController extends Controller
{
    public function index()
    {
        $cemeteries = Cemetery::all();
        return view('cemeteries.index', compact('cemeteries'));
    }

    public function create()
    {
        return view('cemeteries.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required',
            'location' => 'required',
            'available_spots' => 'required|integer',
            'supervisor_name' => 'required',
            'supervisor_phone' => 'required',
        ]);

        Cemetery::create($request->all());
        return redirect()->route('cemeteries.index')->with('success', 'Cemetery added.');
    }

    public function show(Cemetery $cemetery)
    {
        return view('cemeteries.show', compact('cemetery'));
    }

    public function edit(Cemetery $cemetery)
    {
        return view('cemeteries.edit', compact('cemetery'));
    }

    public function update(Request $request, Cemetery $cemetery)
    {
        $request->validate([
            'name' => 'required',
            'location' => 'required',
            'available_spots' => 'required|integer',
            'supervisor_name' => 'required',
            'supervisor_phone' => 'required',
        ]);

        $cemetery->update($request->all());
        return redirect()->route('cemeteries.index')->with('success', 'Cemetery updated.');
    }

    public function destroy(Cemetery $cemetery)
    {
        $cemetery->delete();
        return redirect()->route('cemeteries.index')->with('success', 'Cemetery deleted.');
    }
}

