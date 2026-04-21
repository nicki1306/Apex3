import { Component, OnInit, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vehicle-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './vehicle-list.html',
  styleUrl: './vehicle-list.less'
})
export class VehicleListComponent implements OnInit {
  private http = inject(HttpClient);
  vehicles: any[] = [];

  ngOnInit() {
    this.http.get<any[]>('http://localhost:8000/vehicles/').subscribe((data) => {
      this.vehicles = data;
    });
  }
  
  deleteVehicle(id: number) {
    this.http.delete(`http://localhost:8000/vehicles/${id}`).subscribe(() => {
      // Filtro la lista localmente
      this.vehicles = this.vehicles.filter(v => v.id !== id);
    });
  }

}