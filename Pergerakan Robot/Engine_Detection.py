import math

class EuclideanDistTracker:
    def __init__(self):
        # Memfokuskan Posisi
        self.center_points = {}
        # Jumlah ID (Stuck)
        # setiap kali id objek baru terdeteksi, jumlah akan bertambah satu
        self.id_count = 0

    def update(self, objects_rect):
        # Kotak objek dan ids
        objects_bbs_ids = []

        # Dapatkan titik pusat objek baru(Opsional)
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Cari tahu apakah objek itu sudah terdeteksi (Bergerak)
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            # Objek baru terdeteksi, menetapkan ID ke objek itu
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        # Bersihkan kamus dengan titik tengah untuk menghapus IDS yang tidak digunakan lagi
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Perbarui kamus dengan ID yang tidak digunakan dihapus
        self.center_points = new_center_points.copy()
        return objects_bbs_ids

#RUN


