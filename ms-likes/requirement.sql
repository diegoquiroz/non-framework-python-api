CREATE TABLE property_likes (
  id bigint(20) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  property_id int(11) NOT NULL,
  user_id int(11) NOT NULL
  CONSTRAINT property_likes_property_id_fk FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE;
  CONSTRAINT property_likes_user_id_fk FOREIGN KEY (user_id) REFERENCES auth_user (id) ON DELETE CASCADE;
) ENGINE=InnoDB;


CREATE INDEX property_likes_property_id_fk ON property_likes (property_id);

CREATE INDEX property_likes_user_id_fk ON property_likes (user_id);
