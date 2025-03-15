<?php

namespace App\Http\Controllers;

use App\Models\Deceased;
use App\Models\Cemetery;
use Illuminate\Http\Request;

class DeceasedController extends Controller
{
    public function index()
    {
        $deceased = Deceased::with('cemetery')->get();
        return view('deceased.index', compact('deceased'));
    }

    public function create()
    {
        $cemeteries = Cemetery::all();
        return view('deceased.create', compact('cemeteries'));
    }

    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required',
            'surname' => 'required',
            'region' => 'required',
            'district' => 'required',
            'city' => 'required',
            'cemetery_id' => 'required|exists:cemeteries,id',
            'date_received' => 'required|date',
            'address' => 'required',
        ]);

        Deceased::create($request->all());
        return redirect()->route('deceased.index')->with('success', 'Deceased record added.');
    }

    public function show(Deceased $deceased)
    {
        return view('deceased.show', compact('deceased'));
    }

    public function edit(Deceased $deceased)
    {
        $cemeteries = Cemetery::all();
        return view('deceased.edit', compact('deceased', 'cemeteries'));
    }

    public function update(Request $request, Deceased $deceased)
    {
        $request->validate([
            'name' => 'required',
            'surname' => 'required',
            'region' => 'required',
            'district' => 'required',
            'city' => 'required',
            'cemetery_id' => 'required|exists:cemeteries,id',
            'date_received' => 'required|date',
            'address' => 'required',
        ]);

        $deceased->update($request->all());
        return redirect()->route('deceased.index')->with('success', 'Deceased record updated.');
    }

    public function destroy(Deceased $deceased)
    {
        $deceased->delete();
        return redirect()->route('deceased.index')->with('success', 'Deceased record deleted.');
    }
}


