import { Component, inject} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-vehicle-form',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './vehicle-form.html',
  styleUrl: './vehicle-form.less',
})
export class VehicleForm {

  private http = inject(HttpClient)
  newVehicle = {
    brand: '',
    model: '',
    plate_number: ''
  }
  createVehicle() {
      this.http.post('http://localhost:8000/vehicles/', this.newVehicle).subscribe(() => {
        alert('¡Auto guardado!');
        
        this.newVehicle = { brand: '', model: '', plate_number: '' };
      
      });
    }
}


