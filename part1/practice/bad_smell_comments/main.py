class Unit:
    
    def move(self, field, x: int, y: int, direction, is_fly: bool, is_crawl, points_shift=1):

        if is_fly and is_crawl:  
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:  
            points_shift *= 1.2
            if direction == 'UP':  
                new_y = y + points_shift
                new_x = x  
            elif direction == 'DOWN':  
                new_y = y - points_shift
                new_x = x  
            elif direction == 'LEFT':  
                new_y = y  
                new_x = x - points_shift
            elif direction == 'RIGHT':  
                new_y = y  
                new_x = x + points_shift
        if is_crawl:
            points_shift *= 0.5
            if direction == 'UP':  
                new_y = y + points_shift
                new_x = x  
            elif direction == 'DOWN':  
                new_y = y - points_shift
                new_x = x  
            elif direction == 'LEFT':  
                new_y = y  
                new_x = x - points_shift
            elif direction == 'RIGHT':  
                new_y = y  
                new_x = x + points_shift

            field.set_unit(x=new_x, y=new_y, unit=self)


